%define upstream_name	 DBD-SQLite
%define upstream_version 1.29

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 3

Summary:	Self Contained RDBMS in a DBI Driver
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBI) >= 1.30.0
BuildRequires:  sqlite3-devel	
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

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

