#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-strucchange
Version  : 1.5.2
Release  : 31
URL      : https://cran.r-project.org/src/contrib/strucchange_1.5-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/strucchange_1.5-2.tar.gz
Summary  : Testing, Monitoring, and Dating Structural Changes
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-strucchange-lib = %{version}-%{release}
Requires: R-sandwich
Requires: R-zoo
BuildRequires : R-sandwich
BuildRequires : R-zoo
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-strucchange package.
Group: Libraries

%description lib
lib components for the R-strucchange package.


%prep
%setup -q -c -n strucchange

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570913018

%install
export SOURCE_DATE_EPOCH=1570913018
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library strucchange
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library strucchange
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library strucchange
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc strucchange || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/strucchange/CITATION
/usr/lib64/R/library/strucchange/DESCRIPTION
/usr/lib64/R/library/strucchange/INDEX
/usr/lib64/R/library/strucchange/Meta/Rd.rds
/usr/lib64/R/library/strucchange/Meta/data.rds
/usr/lib64/R/library/strucchange/Meta/demo.rds
/usr/lib64/R/library/strucchange/Meta/features.rds
/usr/lib64/R/library/strucchange/Meta/hsearch.rds
/usr/lib64/R/library/strucchange/Meta/links.rds
/usr/lib64/R/library/strucchange/Meta/nsInfo.rds
/usr/lib64/R/library/strucchange/Meta/package.rds
/usr/lib64/R/library/strucchange/Meta/vignette.rds
/usr/lib64/R/library/strucchange/NAMESPACE
/usr/lib64/R/library/strucchange/NEWS
/usr/lib64/R/library/strucchange/R/strucchange
/usr/lib64/R/library/strucchange/R/strucchange.rdb
/usr/lib64/R/library/strucchange/R/strucchange.rdx
/usr/lib64/R/library/strucchange/data/Rdata.rdb
/usr/lib64/R/library/strucchange/data/Rdata.rds
/usr/lib64/R/library/strucchange/data/Rdata.rdx
/usr/lib64/R/library/strucchange/demo/tkmonitoring.R
/usr/lib64/R/library/strucchange/demo/tktesting.R
/usr/lib64/R/library/strucchange/doc/index.html
/usr/lib64/R/library/strucchange/doc/strucchange-intro.R
/usr/lib64/R/library/strucchange/doc/strucchange-intro.Rnw
/usr/lib64/R/library/strucchange/doc/strucchange-intro.pdf
/usr/lib64/R/library/strucchange/help/AnIndex
/usr/lib64/R/library/strucchange/help/aliases.rds
/usr/lib64/R/library/strucchange/help/paths.rds
/usr/lib64/R/library/strucchange/help/strucchange.rdb
/usr/lib64/R/library/strucchange/help/strucchange.rdx
/usr/lib64/R/library/strucchange/html/00Index.html
/usr/lib64/R/library/strucchange/html/R.css
/usr/lib64/R/library/strucchange/tests/Examples/strucchange-Ex.Rout.save
/usr/lib64/R/library/strucchange/tests/strucchange-tests.R
/usr/lib64/R/library/strucchange/tests/strucchange-tests.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/strucchange/libs/strucchange.so
/usr/lib64/R/library/strucchange/libs/strucchange.so.avx2
