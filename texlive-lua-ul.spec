%global tl_name lua-ul
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.1
Release:	%{tl_revision}.1
Summary:	Underlining for LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/lua-ul
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-ul.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-ul.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-ul.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides underlining, strikethough, and highlighting using
features in LuaLaTeX which avoid the restrictions imposed by other
methods. In particular, kerning is not affected, the underlined text can
use arbitrary commands, hyphenation works etc. The package requires
LuaTeX version [?] 1.12.0.

