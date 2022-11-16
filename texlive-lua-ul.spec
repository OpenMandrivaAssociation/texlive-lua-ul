Name:		texlive-lua-ul
Version:	63469
Release:	1
Summary:	Underlining for LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lua-ul
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-ul.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-ul.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-ul.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides underlining, strikethough, and
highlighting using features in LuaLaTeX which avoid the
restrictions imposed by other methods. In particular, kerning
is not affected, the underlined text can use arbitrary
commands, hyphenation works etc. The package requires LuaTeX
version [?] 1.12.0.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/lua-ul
%{_texmfdistdir}/tex/lualatex/lua-ul
%doc %{_texmfdistdir}/doc/lualatex/lua-ul

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
