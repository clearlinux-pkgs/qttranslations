#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qttranslations
Version  : 5.15.0
Release  : 23
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.0/submodules/qttranslations-everywhere-src-5.15.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.0/submodules/qttranslations-everywhere-src-5.15.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: qttranslations-data = %{version}-%{release}
Requires: qttranslations-license = %{version}-%{release}
BuildRequires : buildreq-qmake
BuildRequires : qttools-dev

%description
All translations are contributed by the Qt community.
They are provided without guarantees, will often be stale, and may even
disappear entirely from future Qt releases.

%package data
Summary: data components for the qttranslations package.
Group: Data

%description data
data components for the qttranslations package.


%package license
Summary: license components for the qttranslations package.
Group: Default

%description license
license components for the qttranslations package.


%prep
%setup -q -n qttranslations-everywhere-src-5.15.0
cd %{_builddir}/qttranslations-everywhere-src-5.15.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1589481698
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qttranslations
cp %{_builddir}/qttranslations-everywhere-src-5.15.0/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qttranslations/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qt5/translations/assistant_ar.qm
/usr/share/qt5/translations/assistant_bg.qm
/usr/share/qt5/translations/assistant_cs.qm
/usr/share/qt5/translations/assistant_da.qm
/usr/share/qt5/translations/assistant_de.qm
/usr/share/qt5/translations/assistant_en.qm
/usr/share/qt5/translations/assistant_es.qm
/usr/share/qt5/translations/assistant_fr.qm
/usr/share/qt5/translations/assistant_hu.qm
/usr/share/qt5/translations/assistant_ja.qm
/usr/share/qt5/translations/assistant_ko.qm
/usr/share/qt5/translations/assistant_pl.qm
/usr/share/qt5/translations/assistant_ru.qm
/usr/share/qt5/translations/assistant_sk.qm
/usr/share/qt5/translations/assistant_sl.qm
/usr/share/qt5/translations/assistant_uk.qm
/usr/share/qt5/translations/assistant_zh_CN.qm
/usr/share/qt5/translations/assistant_zh_TW.qm
/usr/share/qt5/translations/designer_ar.qm
/usr/share/qt5/translations/designer_bg.qm
/usr/share/qt5/translations/designer_cs.qm
/usr/share/qt5/translations/designer_da.qm
/usr/share/qt5/translations/designer_de.qm
/usr/share/qt5/translations/designer_en.qm
/usr/share/qt5/translations/designer_es.qm
/usr/share/qt5/translations/designer_fr.qm
/usr/share/qt5/translations/designer_hu.qm
/usr/share/qt5/translations/designer_ja.qm
/usr/share/qt5/translations/designer_ko.qm
/usr/share/qt5/translations/designer_pl.qm
/usr/share/qt5/translations/designer_ru.qm
/usr/share/qt5/translations/designer_sk.qm
/usr/share/qt5/translations/designer_sl.qm
/usr/share/qt5/translations/designer_uk.qm
/usr/share/qt5/translations/designer_zh_CN.qm
/usr/share/qt5/translations/designer_zh_TW.qm
/usr/share/qt5/translations/linguist_ar.qm
/usr/share/qt5/translations/linguist_bg.qm
/usr/share/qt5/translations/linguist_cs.qm
/usr/share/qt5/translations/linguist_da.qm
/usr/share/qt5/translations/linguist_de.qm
/usr/share/qt5/translations/linguist_en.qm
/usr/share/qt5/translations/linguist_es.qm
/usr/share/qt5/translations/linguist_fr.qm
/usr/share/qt5/translations/linguist_hu.qm
/usr/share/qt5/translations/linguist_it.qm
/usr/share/qt5/translations/linguist_ja.qm
/usr/share/qt5/translations/linguist_ko.qm
/usr/share/qt5/translations/linguist_pl.qm
/usr/share/qt5/translations/linguist_ru.qm
/usr/share/qt5/translations/linguist_sk.qm
/usr/share/qt5/translations/linguist_sl.qm
/usr/share/qt5/translations/linguist_sv.qm
/usr/share/qt5/translations/linguist_uk.qm
/usr/share/qt5/translations/linguist_zh_CN.qm
/usr/share/qt5/translations/linguist_zh_TW.qm
/usr/share/qt5/translations/qt_ar.qm
/usr/share/qt5/translations/qt_bg.qm
/usr/share/qt5/translations/qt_ca.qm
/usr/share/qt5/translations/qt_cs.qm
/usr/share/qt5/translations/qt_da.qm
/usr/share/qt5/translations/qt_de.qm
/usr/share/qt5/translations/qt_en.qm
/usr/share/qt5/translations/qt_es.qm
/usr/share/qt5/translations/qt_fa.qm
/usr/share/qt5/translations/qt_fi.qm
/usr/share/qt5/translations/qt_fr.qm
/usr/share/qt5/translations/qt_gd.qm
/usr/share/qt5/translations/qt_gl.qm
/usr/share/qt5/translations/qt_he.qm
/usr/share/qt5/translations/qt_help_ar.qm
/usr/share/qt5/translations/qt_help_bg.qm
/usr/share/qt5/translations/qt_help_ca.qm
/usr/share/qt5/translations/qt_help_cs.qm
/usr/share/qt5/translations/qt_help_da.qm
/usr/share/qt5/translations/qt_help_de.qm
/usr/share/qt5/translations/qt_help_en.qm
/usr/share/qt5/translations/qt_help_es.qm
/usr/share/qt5/translations/qt_help_fr.qm
/usr/share/qt5/translations/qt_help_gl.qm
/usr/share/qt5/translations/qt_help_hu.qm
/usr/share/qt5/translations/qt_help_it.qm
/usr/share/qt5/translations/qt_help_ja.qm
/usr/share/qt5/translations/qt_help_ko.qm
/usr/share/qt5/translations/qt_help_pl.qm
/usr/share/qt5/translations/qt_help_ru.qm
/usr/share/qt5/translations/qt_help_sk.qm
/usr/share/qt5/translations/qt_help_sl.qm
/usr/share/qt5/translations/qt_help_uk.qm
/usr/share/qt5/translations/qt_help_zh_CN.qm
/usr/share/qt5/translations/qt_help_zh_TW.qm
/usr/share/qt5/translations/qt_hu.qm
/usr/share/qt5/translations/qt_it.qm
/usr/share/qt5/translations/qt_ja.qm
/usr/share/qt5/translations/qt_ko.qm
/usr/share/qt5/translations/qt_lt.qm
/usr/share/qt5/translations/qt_lv.qm
/usr/share/qt5/translations/qt_pl.qm
/usr/share/qt5/translations/qt_pt.qm
/usr/share/qt5/translations/qt_ru.qm
/usr/share/qt5/translations/qt_sk.qm
/usr/share/qt5/translations/qt_sl.qm
/usr/share/qt5/translations/qt_sv.qm
/usr/share/qt5/translations/qt_uk.qm
/usr/share/qt5/translations/qt_zh_CN.qm
/usr/share/qt5/translations/qt_zh_TW.qm
/usr/share/qt5/translations/qtbase_ar.qm
/usr/share/qt5/translations/qtbase_bg.qm
/usr/share/qt5/translations/qtbase_ca.qm
/usr/share/qt5/translations/qtbase_cs.qm
/usr/share/qt5/translations/qtbase_da.qm
/usr/share/qt5/translations/qtbase_de.qm
/usr/share/qt5/translations/qtbase_en.qm
/usr/share/qt5/translations/qtbase_es.qm
/usr/share/qt5/translations/qtbase_fi.qm
/usr/share/qt5/translations/qtbase_fr.qm
/usr/share/qt5/translations/qtbase_gd.qm
/usr/share/qt5/translations/qtbase_he.qm
/usr/share/qt5/translations/qtbase_hu.qm
/usr/share/qt5/translations/qtbase_it.qm
/usr/share/qt5/translations/qtbase_ja.qm
/usr/share/qt5/translations/qtbase_ko.qm
/usr/share/qt5/translations/qtbase_lv.qm
/usr/share/qt5/translations/qtbase_pl.qm
/usr/share/qt5/translations/qtbase_ru.qm
/usr/share/qt5/translations/qtbase_sk.qm
/usr/share/qt5/translations/qtbase_uk.qm
/usr/share/qt5/translations/qtbase_zh_TW.qm
/usr/share/qt5/translations/qtconnectivity_bg.qm
/usr/share/qt5/translations/qtconnectivity_ca.qm
/usr/share/qt5/translations/qtconnectivity_da.qm
/usr/share/qt5/translations/qtconnectivity_de.qm
/usr/share/qt5/translations/qtconnectivity_en.qm
/usr/share/qt5/translations/qtconnectivity_es.qm
/usr/share/qt5/translations/qtconnectivity_hu.qm
/usr/share/qt5/translations/qtconnectivity_ko.qm
/usr/share/qt5/translations/qtconnectivity_pl.qm
/usr/share/qt5/translations/qtconnectivity_ru.qm
/usr/share/qt5/translations/qtconnectivity_uk.qm
/usr/share/qt5/translations/qtdeclarative_bg.qm
/usr/share/qt5/translations/qtdeclarative_da.qm
/usr/share/qt5/translations/qtdeclarative_de.qm
/usr/share/qt5/translations/qtdeclarative_en.qm
/usr/share/qt5/translations/qtdeclarative_es.qm
/usr/share/qt5/translations/qtdeclarative_fi.qm
/usr/share/qt5/translations/qtdeclarative_fr.qm
/usr/share/qt5/translations/qtdeclarative_hu.qm
/usr/share/qt5/translations/qtdeclarative_ja.qm
/usr/share/qt5/translations/qtdeclarative_ko.qm
/usr/share/qt5/translations/qtdeclarative_lv.qm
/usr/share/qt5/translations/qtdeclarative_pl.qm
/usr/share/qt5/translations/qtdeclarative_ru.qm
/usr/share/qt5/translations/qtdeclarative_sk.qm
/usr/share/qt5/translations/qtdeclarative_uk.qm
/usr/share/qt5/translations/qtlocation_bg.qm
/usr/share/qt5/translations/qtlocation_ca.qm
/usr/share/qt5/translations/qtlocation_da.qm
/usr/share/qt5/translations/qtlocation_de.qm
/usr/share/qt5/translations/qtlocation_en.qm
/usr/share/qt5/translations/qtlocation_es.qm
/usr/share/qt5/translations/qtlocation_fi.qm
/usr/share/qt5/translations/qtlocation_fr.qm
/usr/share/qt5/translations/qtlocation_hu.qm
/usr/share/qt5/translations/qtlocation_ko.qm
/usr/share/qt5/translations/qtlocation_pl.qm
/usr/share/qt5/translations/qtlocation_ru.qm
/usr/share/qt5/translations/qtlocation_uk.qm
/usr/share/qt5/translations/qtmultimedia_ar.qm
/usr/share/qt5/translations/qtmultimedia_bg.qm
/usr/share/qt5/translations/qtmultimedia_ca.qm
/usr/share/qt5/translations/qtmultimedia_cs.qm
/usr/share/qt5/translations/qtmultimedia_da.qm
/usr/share/qt5/translations/qtmultimedia_de.qm
/usr/share/qt5/translations/qtmultimedia_en.qm
/usr/share/qt5/translations/qtmultimedia_es.qm
/usr/share/qt5/translations/qtmultimedia_fi.qm
/usr/share/qt5/translations/qtmultimedia_fr.qm
/usr/share/qt5/translations/qtmultimedia_hu.qm
/usr/share/qt5/translations/qtmultimedia_it.qm
/usr/share/qt5/translations/qtmultimedia_ja.qm
/usr/share/qt5/translations/qtmultimedia_ko.qm
/usr/share/qt5/translations/qtmultimedia_pl.qm
/usr/share/qt5/translations/qtmultimedia_ru.qm
/usr/share/qt5/translations/qtmultimedia_sk.qm
/usr/share/qt5/translations/qtmultimedia_uk.qm
/usr/share/qt5/translations/qtmultimedia_zh_TW.qm
/usr/share/qt5/translations/qtquickcontrols2_ar.qm
/usr/share/qt5/translations/qtquickcontrols2_bg.qm
/usr/share/qt5/translations/qtquickcontrols2_ca.qm
/usr/share/qt5/translations/qtquickcontrols2_da.qm
/usr/share/qt5/translations/qtquickcontrols2_en.qm
/usr/share/qt5/translations/qtquickcontrols2_hu.qm
/usr/share/qt5/translations/qtquickcontrols2_ko.qm
/usr/share/qt5/translations/qtquickcontrols2_uk.qm
/usr/share/qt5/translations/qtquickcontrols2_zh_TW.qm
/usr/share/qt5/translations/qtquickcontrols_bg.qm
/usr/share/qt5/translations/qtquickcontrols_ca.qm
/usr/share/qt5/translations/qtquickcontrols_da.qm
/usr/share/qt5/translations/qtquickcontrols_de.qm
/usr/share/qt5/translations/qtquickcontrols_en.qm
/usr/share/qt5/translations/qtquickcontrols_fi.qm
/usr/share/qt5/translations/qtquickcontrols_fr.qm
/usr/share/qt5/translations/qtquickcontrols_ja.qm
/usr/share/qt5/translations/qtquickcontrols_ru.qm
/usr/share/qt5/translations/qtquickcontrols_uk.qm
/usr/share/qt5/translations/qtquickcontrols_zh_TW.qm
/usr/share/qt5/translations/qtscript_ar.qm
/usr/share/qt5/translations/qtscript_bg.qm
/usr/share/qt5/translations/qtscript_ca.qm
/usr/share/qt5/translations/qtscript_cs.qm
/usr/share/qt5/translations/qtscript_da.qm
/usr/share/qt5/translations/qtscript_de.qm
/usr/share/qt5/translations/qtscript_en.qm
/usr/share/qt5/translations/qtscript_es.qm
/usr/share/qt5/translations/qtscript_fi.qm
/usr/share/qt5/translations/qtscript_fr.qm
/usr/share/qt5/translations/qtscript_he.qm
/usr/share/qt5/translations/qtscript_hu.qm
/usr/share/qt5/translations/qtscript_it.qm
/usr/share/qt5/translations/qtscript_ja.qm
/usr/share/qt5/translations/qtscript_ko.qm
/usr/share/qt5/translations/qtscript_lv.qm
/usr/share/qt5/translations/qtscript_pl.qm
/usr/share/qt5/translations/qtscript_ru.qm
/usr/share/qt5/translations/qtscript_sk.qm
/usr/share/qt5/translations/qtscript_uk.qm
/usr/share/qt5/translations/qtserialport_de.qm
/usr/share/qt5/translations/qtserialport_en.qm
/usr/share/qt5/translations/qtserialport_es.qm
/usr/share/qt5/translations/qtserialport_ja.qm
/usr/share/qt5/translations/qtserialport_ko.qm
/usr/share/qt5/translations/qtserialport_pl.qm
/usr/share/qt5/translations/qtserialport_ru.qm
/usr/share/qt5/translations/qtserialport_uk.qm
/usr/share/qt5/translations/qtwebengine_ca.qm
/usr/share/qt5/translations/qtwebengine_de.qm
/usr/share/qt5/translations/qtwebengine_en.qm
/usr/share/qt5/translations/qtwebengine_es.qm
/usr/share/qt5/translations/qtwebengine_ko.qm
/usr/share/qt5/translations/qtwebengine_pl.qm
/usr/share/qt5/translations/qtwebengine_ru.qm
/usr/share/qt5/translations/qtwebengine_uk.qm
/usr/share/qt5/translations/qtwebsockets_ca.qm
/usr/share/qt5/translations/qtwebsockets_de.qm
/usr/share/qt5/translations/qtwebsockets_en.qm
/usr/share/qt5/translations/qtwebsockets_es.qm
/usr/share/qt5/translations/qtwebsockets_fr.qm
/usr/share/qt5/translations/qtwebsockets_ja.qm
/usr/share/qt5/translations/qtwebsockets_ko.qm
/usr/share/qt5/translations/qtwebsockets_pl.qm
/usr/share/qt5/translations/qtwebsockets_ru.qm
/usr/share/qt5/translations/qtwebsockets_uk.qm
/usr/share/qt5/translations/qtxmlpatterns_bg.qm
/usr/share/qt5/translations/qtxmlpatterns_ca.qm
/usr/share/qt5/translations/qtxmlpatterns_cs.qm
/usr/share/qt5/translations/qtxmlpatterns_da.qm
/usr/share/qt5/translations/qtxmlpatterns_de.qm
/usr/share/qt5/translations/qtxmlpatterns_en.qm
/usr/share/qt5/translations/qtxmlpatterns_es.qm
/usr/share/qt5/translations/qtxmlpatterns_fr.qm
/usr/share/qt5/translations/qtxmlpatterns_hu.qm
/usr/share/qt5/translations/qtxmlpatterns_it.qm
/usr/share/qt5/translations/qtxmlpatterns_ja.qm
/usr/share/qt5/translations/qtxmlpatterns_ko.qm
/usr/share/qt5/translations/qtxmlpatterns_pl.qm
/usr/share/qt5/translations/qtxmlpatterns_ru.qm
/usr/share/qt5/translations/qtxmlpatterns_sk.qm
/usr/share/qt5/translations/qtxmlpatterns_uk.qm
/usr/share/qt5/translations/qtxmlpatterns_zh_TW.qm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qttranslations/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
