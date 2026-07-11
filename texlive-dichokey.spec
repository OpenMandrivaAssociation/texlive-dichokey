%global tl_name dichokey
%global tl_revision 17192

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Construct dichotomous identification keys
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dichokey
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dichokey.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dichokey.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package can be used to construct dichotomous identification keys
(used especially in biology for species identification), taking care of
numbering and indentation of successive key steps automatically. An
example file is provided, which demonstrates usage.

