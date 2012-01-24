%define upstream_name	 DBD-SQLite
%define upstream_version 1.36

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 0.2

Summary:	Self Contained RDBMS in a DBI Driver
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/%{upstream_name}-%{upstream_version}_01.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(DBI) >= 1.616.0-5
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec) >= 0.820.0
BuildRequires:	perl(Test::Builder) >= 0.860.0
BuildRequires:	perl(Test::More) >= 0.470.0
BuildRequires:	perl(Tie::Hash)
BuildRequires:  sqlite3-devel >= 3.6.0
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
%setup -q -n %{upstream_name}-%{upstream_version}_01

# force it to use the system sqlite lib
rm -f sqlite3.c sqlite3.h

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor LIBS="-L%{_libdir} -lsqlite3"
%make CCFLAGS="%{optflags} -DNDEBUG=1 -DSQLITE_PTR_SZ=4"

%check
%{__make} test LIBS="-L%{_libdir} -lsqlite3"

%install
rm -rf %{buildroot}
%makeinstall_std

# useless content
rm -f %{buildroot}%{perl_vendorarch}/auto/share/dist/DBD-SQLite/sqlite3.c
rm -f %{buildroot}%{perl_vendorarch}/auto/share/dist/DBD-SQLite/sqlite3.h

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README* Changes
%{perl_vendorarch}/DBD
%{perl_vendorarch}/auto/DBD
%{_mandir}/*/*

