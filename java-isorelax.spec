Summary:	ISO RELAX interface
Summary(pl.UTF-8):	Interfejs ISO RELAX
Name:		java-isorelax
Version:	20041111
Release:	1
License:	MIT
Group:		Libraries/Java
Source0:	http://downloads.sourceforge.net/iso-relax/isorelax.%{version}.zip
# Source0-md5:	10381903828d30e36252910679fcbab6
URL:		http://iso-relax.sourceforge.net/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is to define/share/maintain codes and documents related
to ISO RELAX. In particular, interface definitions which are necessary
for RELAX-related programs to interoperate, reference implementations,
and concept implementations.

%description -l pl.UTF-8
Ten projekt ma na celu zdefiniowanie i utrzymywanie kodu oraz
dokumentów związanych z ISO RELAX. W szczególności definicji
interfejsów niezbędnych dla programów związanych z ISO RELAX do
współpracy, implementacji wzorcowych oraz implementacji założeń.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -p isorelax.jar $RPM_BUILD_ROOT%{_javadir}/isorelax-%{version}.jar
ln -s isorelax-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/isorelax.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.txt
%{_javadir}/isorelax-%{version}.jar
%{_javadir}/isorelax.jar
