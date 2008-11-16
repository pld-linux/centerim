# TODO
# - use system libgadu (then remove libjpeg BR)
# - WARNING: No GPG support in Jabber, since GPGME library not found or its setup not ok
Summary:	Console ncurses based IM (ICQ, Yahoo!, MSN, AIM, IRC) client
Summary(es.UTF-8):	CenterIM es un cliente ICQ basado en ncurses para el modo texto
Summary(pl.UTF-8):	Klient IM (ICQ, Yahoo!, MSN, AIM, IRC) w wersji tekstowej
Summary(pt_BR.UTF-8):	O centerIM é um cliente ICQ baseado em ncurses para o modo texto
Name:		centerim
Version:	4.22.2
Release:	2
License:	GPL v2+
Group:		Applications/Communications
Source0:	http://www.centerim.org/download/releases/%{name}-%{version}.tar.gz
# Source0-md5:	dcced736e2f261e08e667403c42dc78f
URL:		http://www.centerim.org/
BuildRequires:	curl-devel >= 4.12.0
BuildRequires:	fribidi-devel
BuildRequires:	gettext-devel
# tested, but HAVE_GPGME never defined because of test->text typo
#BuildRequires:	gpgme-devel >= 0.4.2
BuildRequires:	libjpeg-devel
# not enabled
#BuildRequires:	libotr-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
Obsoletes:	centerICQ
Obsoletes:	centericq < 4.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CenterIM is a text mode menu- and window-driven IM interface.
Currently ICQ2000, Yahoo!, MSN, AIM TOC and IRC protocols are
supported. It allows you to send, receive, and forward messages, URLs
and, SMSes, mass message send, search for users (including extended
"whitepages search"), view users' details, maintain your contact list
directly from the program (including non-icq contacts), view the
messages history, register a new UIN and update your details, be
informed on receiving email messages, automatically set away after the
defined period of inactivity (on any console), and have your own
ignore, visible and invisible lists. It can also associate events with
sounds, has support for Hebrew and Arabic languages and allows to
arrange contacts into groups.

%description -l pl.UTF-8
CenterIM to tekstowy, sterowany za pomocą menu i okien interfejs do
protokołów IM. Aktualnie obsługuje protokoły ICQ2000, Yahoo!, MSN,
AIM TOC oraz IRC. Pozwala na wysyłanie, odbiór oraz przesyłanie
dalej wiadomości, adresów i kontaktów, wysyłanie wielu wiadomości
naraz, przeglądanie informacji o innych użytkownikach, rejestrację
nowego UINu oraz uzupełnianie swoich informacji, informowanie o
nadejściu nowej poczty, włączanie automatycznego stanu Away po
wybranym czasie nieaktywności (na dowolnej konsoli!), posiadanie
własnej listy osób ignorowanych. Może także powiązać zdarzenia z
dźwiękami.

%description -l pt_BR.UTF-8
O CenterIM é um cliente ICQ baseado em ncurses para o modo texto.

%prep
%setup -q

%build
CXXFLAGS="-I/usr/include/ncurses %{rpmcflags}"
%configure \
	ac_cv_lib_nsl_gethostbyname=no \
	--with-openssl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh_TW.Big5,zh_TW}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/centerim
%attr(755,root,root) %{_bindir}/cimconv
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.wav
%{_mandir}/man1/centerim.1*
%{_mandir}/man1/cimconv.1*
