%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	Combination
Summary:	List::Combination - an iterator over the combinations of an array
Summary(pl):	List::Combination - iterator po kombinacjach tablicy
Name:		perl-List-Combination
Version:	1.00
Release:	2
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.pm.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides the ability to iterate over all the combinations,
of a given size, of the objects in an array.

%description -l pl
Ta klasa daje mo¿liwo¶æ iterowania po wszystkich (danej d³ugo¶ci)
kombinacjach obiektów tablicy.

%prep
%setup -q -n %{name}-%{version} -c -T
%{__gzip} -dc %{_sourcedir}/List-Combination-%{version}.pm.gz > Combination.pm

%build
touch Makefile.PL
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"List::Combination");' \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
