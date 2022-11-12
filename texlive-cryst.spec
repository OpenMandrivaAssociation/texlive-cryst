Name:		texlive-cryst
Version:	15878
Release:	1
Summary:	Font for graphical symbols used in crystallography
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cryst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cryst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cryst.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The font is provided as an Adobe Type 1 font, and as MetaFont
source. Instructions for use are available both in the README
file and (with a font diagram) in the documentation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/cryst/cryst.afm
%{_texmfdistdir}/fonts/source/public/cryst/cryst.mf
%{_texmfdistdir}/fonts/tfm/public/cryst/cryst.tfm
%{_texmfdistdir}/fonts/type1/public/cryst/cryst.pfb
%doc %{_texmfdistdir}/doc/latex/cryst/README
%doc %{_texmfdistdir}/doc/latex/cryst/cryst1.pdf
%doc %{_texmfdistdir}/doc/latex/cryst/cryst1.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
