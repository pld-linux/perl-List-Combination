%define		pdir	List
%define		pnam	Combination
%include	/usr/lib/rpm/macros.perl
Summary:	List::Combination - an iterator over the combinations of an array
Summary(pl.UTF-8):	List::Combination - iterator po kombinacjach tablicy
Name:		perl-List-Combination
Version:	1.00
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.pm.gz
# Source0-md5:	15f3e07012320c5a1c9d91f40ac03550
URL:		http://search.cpan.org/dist/List-Combination/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides the ability to iterate over all the combinations,
of a given size, of the objects in an array.

%description -l pl.UTF-8
Ta klasa daje możliwość iterowania po wszystkich (danej długości)
kombinacjach obiektów tablicy.

%prep
%setup -q -c -T
%{__gzip} -dc %{_sourcedir}/List-Combination-%{version}.pm.gz > Combination.pm

%build
touch Makefile.PL
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"List::Combination");' \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
