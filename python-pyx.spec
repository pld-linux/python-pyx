%define 	module	pyx
Summary:	Python package for the creation of PostScript and PDF files
Summary(pl):	Pakiet dla Pythona do tworzenia plików PostScript i PDF
Name:		python-%{module}
Version:	0.8.1
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyx/PyX-%{version}.tar.gz
# Source0-md5:	5e751cef8d62774a6fc659cc9a03c231
URL:		http://pyx.sourceforge.net/
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyX is a Python package for the creation of PostScript and PDF files.
It combines an abstraction of the PostScript drawing model with a
TeX/LaTeX interface. Complex tasks like 2D and 3D plots in
publication-ready quality are built out of these primitives.

%description -l pl
PyX to pakiet Pythona do tworzenia plików PostScript i PDF. £±czy
abstrakcjê modelu rysowania PostScriptu z interfejsem
TeXowym/LaTeXowym. Z³o¿one zadania takie jak wykresy 2D i 3D o jako¶ci
nadaj±cej siê do publikacji s± tworzone z takich prymitywów.

%prep
%setup -q -n PyX-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

#Fixing paths
sed -e "s@$RPM_BUILD_ROOT@@g" -i $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/siteconfig.py

#Removing *.py files
mv $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/siteconfig.py $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/siteconfig.py.bak
rm -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/siteconfig.py[o,c]
find $RPM_BUILD_ROOT%{py_scriptdir} -type f -name "*.py"|xargs rm
mv $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/siteconfig.py.bak $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/siteconfig.py


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{py_sitescriptdir}/%{module}
%dir %{_datadir}/%{module}
%{_datadir}/%{module}/*.lfs
%{_datadir}/%{module}/pyx.def
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pyxrc
