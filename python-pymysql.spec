Name:		python-pymysql
Version:	1.1.2
Release:	2
Summary:	Pure Python MySQL Driver
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/pymysql/
Source0:	pymysql-1.1.2.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
Pure Python MySQL Driver.

%files
%{py_sitedir}/*
