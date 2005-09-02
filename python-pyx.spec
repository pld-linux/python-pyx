%define 	module	pyx
Summary:	Python package for the creation of PostScript and PDF files
Summary(pl):	Pakiet dla Pythona do tworzenia plików PostScript i PDF
Name:		python-%{module}
Version:	0.8.1
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyx/PyX-%{version}.tar.gz
URL:		http://pyx.sourceforge.net/
%pyrequires_eq	python-modules
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_scriptdir} -type f -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc AUTHORS README
# %dir %{py_sitedir}/%{module}
%{py_sitescriptdir}/%{module}
%dir %{_datadir}/%{module}
%{_datadir}/%{module}/*.lfs
%{_datadir}/%{module}/pyx.def
#%attr(755,root,root) %{py_sitedir}/%{module}/*.so
#%{py_sitedir}/%{module}/*.py[co]
%{_sysconfdir}/pyxrc
