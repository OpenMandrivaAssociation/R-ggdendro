%global packname  ggdendro
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.1.14
Release:          1
Summary:          Tools for extracting dendrogram and tree diagram plot data for use with ggplot
Group:            Sciences/Mathematics
License:          GPLv2+
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-14.tar.gz


Requires:         R-MASS R-ggplot2 
Requires:         R-rpart R-tree 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-MASS R-ggplot2 
BuildRequires:   R-rpart R-tree 
%description
This is a set of tools for dendrograms and tree plots using ggplot.  The
ggplot philosophy is to clearly separate data from the presentation.
Unfortunately the plot method for dendrograms plots directly to a plot
device without exposing the data. The ggdendro package resolves this by
making available functions that extract the dendrogram plot data.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
