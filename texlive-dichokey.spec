Name:		texlive-dichokey
Version:	17192
Release:	2
Summary:	Construct dichotomous identification keys
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dichokey
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dichokey.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dichokey.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package can be used to construct dichotomous identification
keys (used especially in biology for species identification),
taking care of numbering and indentation of successive key
steps automatically. An example file is provided, which
demonstrates usage.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dichokey/dichokey.sty
%doc %{_texmfdistdir}/doc/latex/dichokey/dichokey.pdf
%doc %{_texmfdistdir}/doc/latex/dichokey/dichokey.tex
%doc %{_texmfdistdir}/doc/latex/dichokey/rhodocyb.pdf
%doc %{_texmfdistdir}/doc/latex/dichokey/rhodocyb.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
