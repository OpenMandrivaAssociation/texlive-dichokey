Name:		texlive-dichokey
Version:	20100223
Release:	1
Summary:	Construct dichotomous identification keys
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dichokey
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dichokey.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dichokey.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package can be used to construct dichotomous identification
keys (used especially in biology for species identification),
taking care of numbering and indentation of successive key
steps automatically. An example file is provided, which
demonstrates usage.

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
%{_texmfdistdir}/tex/latex/dichokey/dichokey.sty
%doc %{_texmfdistdir}/doc/latex/dichokey/dichokey.pdf
%doc %{_texmfdistdir}/doc/latex/dichokey/dichokey.tex
%doc %{_texmfdistdir}/doc/latex/dichokey/rhodocyb.pdf
%doc %{_texmfdistdir}/doc/latex/dichokey/rhodocyb.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
