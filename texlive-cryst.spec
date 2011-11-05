# revision 15878
# category Package
# catalog-ctan /fonts/cryst
# catalog-date 2008-08-15 14:30:40 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-cryst
Version:	20080815
Release:	1
Summary:	Font for graphical symbols used in crystallography
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cryst
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cryst.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cryst.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The font is provided as an Adobe Type 1 font, and as MetaFont
source. Instructions for use are available both in the README
file and (with a font diagram) in the documentation.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
