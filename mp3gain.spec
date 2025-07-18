%define	subver	_r2
Summary:	Analyzes and losslessly adjusts MP3 files to a specified target volume
Summary(pl.UTF-8):	Analiza i bezstratne dostrojenie plików MP3 do zadanej głośności
Name:		mp3gain
Version:	1.5.2
Release:	1
License:	LGPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/mp3gain/%{name}-%(echo %{version} | tr . _)%{subver}-src.zip
# Source0-md5:	b8e429f3225cc298c5d13d31afd050b6
Patch0:		%{name}-Makefile.patch
URL:		http://mp3gain.sourceforge.net/
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MP3Gain analyzes and losslessly adjusts mp3 files to a specified
target volume. It does not simply do peak amplitude normalization.
Instead, it performs statistical analysis to determine how loud the
file actually sounds to the human ear.

%description -l pl.UTF-8
MP3Gain analizuje i bezstratnie dostraja pliki mp3 do zadanej
głośności. Nie przeprowadza zwykłej normalizacji poziomu szczytowego.
Przeprowadza za to analizę statystyczną w celu określenia jak głośno
tak naprawdę plik brzmi dla ludzkiego ucha.

%prep
%setup -q -c
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags}" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install mp3gain $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mp3gain
