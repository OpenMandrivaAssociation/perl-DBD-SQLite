%define module	DBD-SQLite
%define name	perl-%{module}
%define version	1.14
%define release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Self Contained RDBMS in a DBI Driver
License:	GPL
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/%{module}-%{version}.tar.bz2
# http://rt.cpan.org/Public/Bug/Display.html?id=32100
Patch:      perl-DBD-SQLite-1.14-fix-tests.patch
Group:		Development/Perl
BuildRequires:	perl-devel
BuildRequires:	perl(DBI) >= 1.03-1mdk
BuildRequires:  sqlite3-devel	
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
SQLite is a small fast embedded SQL database engine.

DBD::SQLite embeds that database engine into a DBD driver, so
if you want a relational database for your project, but don't
want to install a large RDBMS system like MySQL or PostgreSQL,
then DBD::SQLite may be just what you need.

It supports quite a lot of features, such as transactions (atomic
commit and rollback), indexes, DBA-free operation, a large subset
of SQL92 supported, and more.

%prep
%setup -q -n %{module}-%{version}
%patch -p 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CCFLAGS="%{optflags} -DNDEBUG=1 -DSQLITE_PTR_SZ=4"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README* Changes
%{perl_vendorarch}/DBD
%{perl_vendorarch}/auto/DBD
%{_mandir}/*/*



