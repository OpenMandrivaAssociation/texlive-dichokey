# revision 17192
# category Package
# catalog-ctan /macros/latex/contrib/dichokey
# catalog-date 2010-02-23 23:30:05 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-dichokey
Version:	20190228
Release:	1
Summary:	Construct dichotomous identification keys
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dichokey
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dichokey.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dichokey.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100223-2
+ Revision: 750955
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100223-1
+ Revision: 718228
- texlive-dichokey
- texlive-dichokey
- texlive-dichokey
- texlive-dichokey

