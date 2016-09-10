"""Test image and album directives."""

import re

import pytest
from docutils.parsers.rst import directives, roles
from sphinx import application
from sphinx.errors import SphinxWarning

from sphinxcontrib.imgur.directives import ImgurError
from tests.helpers import BASE_CONFIG

TEST_CASES = [
    dict(id='Valid123', hpd_conf=None, hpd_option=None),
    dict(id='Valid123', hpd_conf=False, hpd_option=None),
    dict(id='Valid123', hpd_conf=True, hpd_option=None),
    dict(id='Valid123', hpd_conf=None, hpd_option=False),
    dict(id='Valid123', hpd_conf=False, hpd_option=False),
    dict(id='Valid123', hpd_conf=True, hpd_option=False),
    dict(id='Valid123', hpd_conf=None, hpd_option=True),
    dict(id='Valid123', hpd_conf=False, hpd_option=True),
    dict(id='Valid123', hpd_conf=True, hpd_option=True),
    dict(id='Inv_lid!', hpd_conf=None, hpd_option=None),
    dict(id=None, hpd_conf=None, hpd_option=None),
]


@pytest.mark.usefixtures('reset_sphinx')
@pytest.mark.parametrize('is_album', [True, False])
@pytest.mark.parametrize('test_case', TEST_CASES)
def test(monkeypatch, tmpdir, is_album, test_case):
    """Test valid and invalid values.

    :param monkeypatch: pytest fixture.
    :param tmpdir: pytest fixture.
    :param bool is_album: Test with Imgur album vs image.
    :param dict test_case: Dict from TEST_CASES list.
    """
    # Write conf.py.
    conf_py = tmpdir.join('conf.py')
    conf_py.write(BASE_CONFIG)
    if test_case['hpd_conf'] is not None:
        conf_py.write('imgur_hide_post_details = {}'.format(test_case['hpd_conf']), mode='a')

    # Write index.rst.
    index_rst = tmpdir.join('index.rst')
    index_rst.write('====\nMain\n====\n\n.. toctree::\n    :maxdepth: 2\n.. imgur-embed::')
    if test_case['id'] is not None and is_album:
        index_rst.write(' a/{}'.format(test_case['id']), mode='a')
    elif test_case['id'] is not None:
        index_rst.write(' {}'.format(test_case['id']), mode='a')
    if test_case['hpd_option'] is not None:
        index_rst.write('\n    :hide_post_details: True', mode='a')

    monkeypatch.setattr(directives, '_directives', getattr(directives, '_directives').copy())
    monkeypatch.setattr(roles, '_roles', getattr(roles, '_roles').copy())

    srcdir = confdir = str(tmpdir)
    outdir = tmpdir.join('_build', 'html')
    doctreedir = outdir.join('doctrees').ensure(dir=True, rec=True)
    app = application.Sphinx(srcdir, confdir, str(outdir), str(doctreedir), 'html', warningiserror=True)

    if test_case['id'] == 'Valid123':
        app.builder.build_all()
        html_body = outdir.join('index.html').read()
        blockquotes = re.findall(r'(<blockquote[^>]* class="imgur-embed-pub"[^>]*>)', html_body)
        scripts = re.findall(r'(<script[^>]* src="//s.imgur.com/min/embed.js"[^>]*>)', html_body)
        assert 1 == len(blockquotes)
        assert 1 == len(scripts)
        if is_album:
            assert 'data-id="a/Valid123"' in blockquotes[0]
        else:
            assert 'data-id="Valid123"' in blockquotes[0]
        return

    if test_case['id'] is not None:
        with pytest.raises(ImgurError) as exc:
            app.builder.build_all()
        expected_error = 'Invalid Imgur ID specified. Must be 5-10 letters and numbers. Albums prefixed with "a/".'
        assert expected_error == exc.value.args[0]
        return

    with pytest.raises(SphinxWarning) as exc:
        app.builder.build_all()
    expected_error = '1 argument(s) required, 0 supplied.'
    assert expected_error in exc.value.args[0]