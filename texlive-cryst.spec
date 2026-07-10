%global tl_name cryst
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Font for graphical symbols used in crystallography
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cryst
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cryst.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cryst.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The font is provided as an Adobe Type 1 font, and as Metafont source.
Instructions for use are available both in the README file and (with a
font diagram) in the documentation.

