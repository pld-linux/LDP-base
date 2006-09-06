Summary:	Base directory for LDP documents
Summary(pl):	G��wny katalog dla dokumentacji LDP
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

%description -l pl
Ten pakiet zawiera g��wny katalog dla dokument�w z projektu LDP
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