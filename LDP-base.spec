Summary:	Base directory for LDP documents
Summary(pl.UTF-8):	Główny katalog dla dokumentacji LDP
Name:		LDP-base
Version:	1
Release:	1
License:	GPL
Group:		Base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains base directory for LDP (Linux Documentation
Project) documents.

%description -l pl.UTF-8
Ten pakiet zawiera główny katalog dla dokumentów z projektu LDP
(Linux Documentation Project).

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP
