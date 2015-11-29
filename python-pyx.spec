%define 	module	pyx
Summary:	Python package for the creation of PostScript and PDF files
Summary(pl.UTF-8):	Pakiet dla Pythona do tworzenia plików PostScript i PDF
Name:		python-%{module}
Version:	0.10
Release:	3
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyx/PyX-%{version}.tar.gz
# Source0-md5:	20a8697a4b37c3ead10348ad5a49ba1a
URL:		http://pyx.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyX is a Python package for the creation of PostScript and PDF files.
It combines an abstraction of the PostScript drawing model with a
TeX/LaTeX interface. Complex tasks like 2D and 3D plots in
publication-ready quality are built out of these primitives.

%description -l pl.UTF-8
PyX to pakiet Pythona do tworzenia plików PostScript i PDF. Łączy
abstrakcję modelu rysowania PostScriptu z interfejsem
TeXowym/LaTeXowym. Złożone zadania takie jak wykresy 2D i 3D o jakości
nadającej się do publikacji są tworzone z takich prymitywów.

%prep
%setup -q -n PyX-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

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
