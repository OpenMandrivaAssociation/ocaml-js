%define debug_package %{nil}
%define name ocaml-js
%define srcname js_of_ocaml
%define versionbase 1.0.4
#define releasecandidate rc5
%define release 2
#define versioncomplete %{versionbase}-%{releasecandidate}
%define versioncomplete %{versionbase}

Name:           %{name}
Version:        %{versionbase}
Release:        %{release}
Summary:        OCaml to JavaScript bytecode compiler
Group:          Development/C
License:        GPLv2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:            http://ocsigen.org/js_of_ocaml/manual/
Source0:	http://ocsigen.org/download/%{srcname}-%{version}.tar.gz
# As of 1.0.4, need to change Makefile.conf to set BINDIR to /usr/bin instead of /usr/local/bin
# Also changes install from $(BINDIR) to $(DESTDIR)$(BINDIR)
Patch0:		Makefile-bindir.patch
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:	ocaml-lwt
BuildRequires:  ocaml-doc

%global __ocaml_requires_opts -i Ast_c -i Token_c -i Type_cocci -i Ast_cocci -i Common -i Oassocb -i ANSITerminal -i Oseti -i Sexplib -i Oassoch -i Setb -i Oassoc_buffer -i Ograph2way -i SetPt -i Mapb -i Dumper -i Osetb -i Flag


%description
Js_of_ocaml is a compiler of OCaml bytecode to Javascript. It makes it possible
to run Ocaml programs in a Web browser. Its key features are the following:
 - The whole language, and most of the standard library are supported.
 - The compiler is easy to install: it only depends on Findlib and Lwt.
 - The generated code is independant of Eliom and the Ocsigen server. You can
   use it with any Web server.
 - You can use a standard installation of OCaml to compile your programs. In
   particular, you do not have to recompile a library to use it with
   Js_of_ocaml. You just have to link your program with a specific library to
   interface with the browser APIs. 

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files
%{_bindir}/%{srcname}
%{_libdir}/ocaml/%{srcname}/META
%{_libdir}/ocaml/%{srcname}/*.cma
%{_libdir}/ocaml/%{srcname}/*.cmi
%{_libdir}/ocaml/%{srcname}/*.cmo
%{_libdir}/ocaml/%{srcname}/*.js

%files devel
%{_libdir}/ocaml/%{srcname}/*.a
%{_libdir}/ocaml/stublibs/*.so*

%prep
%setup -q -n %{srcname}-%{versioncomplete}
%apply_patches

%build
make
make doc

%install
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make DESTDIR=%{buildroot} install


