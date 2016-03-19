#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Regexp
%define		pnam	Grammars
Summary:	Regexp::Grammars Perl module - add grammatical parsing features to Perl 5.10 regexes
Summary(pl.UTF-8):	Modu� Perla Regexp::Grammars - dodaje do wyra�e� regularnych mo�liwo�� parsowania gramatyk
Name:		perl-Regexp-Grammars
Version:	1.045
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8d55de81d4985953e25a76a1f28897da
BuildRequires:	perl-devel >= 1:5.10.0
BuildRequires:	perl-Test-Simple >= 0.30
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module Regexp::Grammars adds a small number of new regex constructs
that can be used within Perl 5.10 patterns to implement complete
recursive-descent parsing.

%description -l pl.UTF-8
Modu� Regexp::Grammars dodaje troch� nowych konstrukcji wyra�e�
regularnych, kt�re mog� by� u�yte w Perlu 5.10 do implementacji
kompletnego analizatora zst�puj�cego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Regexp/Grammars.pm
%{_mandir}/man3/*
