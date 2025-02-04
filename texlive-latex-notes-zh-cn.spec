Name:		texlive-latex-notes-zh-cn
Version:	15878
Release:	2
Summary:	Chinese Introduction to TeX and LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/latex-notes-zh-cn
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-notes-zh-cn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-notes-zh-cn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document is an introduction to TeX/LaTeX, in Chinese. It
covers basic text typesetting, mathematics, graphics, tables,
Chinese language & fonts, and some miscellaneous features
(hyperlinks, long documents, bibliographies, indexes and page
layout).

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/README
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/history.txt
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/latex-notes-zh-cn.pdf
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/license.txt
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/basics.tex
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/dscf4684.jpg
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/arrow.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/color.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/colors.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/curve.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/dashed.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/dot.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/fill.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/label.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/line.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/loop.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/path.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/predefined.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_arc.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_arrow.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_axis.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_bezier.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_circle.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_color.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_curve.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_dot.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_fill.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_frame.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_grid.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_label.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_line.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_linestyle.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_origin.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_parabola.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_polygon.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_rput.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/pst_uput.eps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/subfig.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/subfig_left.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/subfig_right.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/transform.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/examples/uline.mps
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/fonts.tex
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/graphics.tex
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/i18n.tex
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/introduction.tex
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/lnotes.tex
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/math.tex
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/misc.tex
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/postcript.tex
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/preface.tex
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/reading.bib
%doc %{_texmfdistdir}/doc/generic/latex-notes-zh-cn/src/tables.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
