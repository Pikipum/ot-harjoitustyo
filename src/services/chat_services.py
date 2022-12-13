import time
from services.dataparser import get_accounts, get_messages, save_to_file, save_accounts

#users = get_accounts()
#messages = get_messages()

#current_user = None


class ChatService:
    """Sovelluslogiikasta vastaava luokka"""

    def __init__(self) -> None:
        self._current_user = None
        self._users = get_accounts()
        self._messages = get_messages()
        self._time = time.localtime()

        """Luokan konstruktori, jossa luokan sisällä käytettävien muuttujien alustus"""

    def current_time_as_string(self):
        """
        Palauttaa ajan Stringinä
        """
        return time.strftime("%H:%M", self._time)

    def stringvar_to_string(self, s):
        """
        Tarkistaa, onko syötetty arvo string vai StringVar.
        Palauttaa syötteen tavallisenä merkkijonona
        """
        if not isinstance(s, str):
            return s.get()
        return s

    def username_exists(self, username):
        """
        Tarkistaa onko username self._usersissa. Jos on, palauttaa 1.
        """
        if username in self._users:
            return 1
        return 0

    def add_user(self, name, password):
        """
        Lisää käyttäjän ja salasanan users-dictionaryyn
        """
        self._users[name] = password

    def check_log_in(self, username, password):
        """
        Hakee käyttäjän käyttäjänimen perusteella users-dictionarystä
        ja tarkastaa onko salasana oikein.
        """
        username = self.stringvar_to_string(username)
        password = self.stringvar_to_string(password)

        if not self.username_exists(username):
            return 0
        if password == self._users.get(username):
            self._current_user = username
            return 1
        return 0

    def create_account(self, username, password):
        """
        Muuttaa kaksi syötettä merkkijonoiksi ja tarkistaa onko username jo dictionaryssa,
        jos ei: luo tili
        """
        username = self.stringvar_to_string(username)
        password = self.stringvar_to_string(password)

        if not username in self._users:
            self.add_user(username, password)
            save_accounts(self._users)
            return 1
        return 0

    def send_message(self, message):
        """
        Muuttaa syötteen merkkijonoksi, lisää sen messages-listan loppuun ja pyytää 
        dataparseria tallentamaan päivitetyn historian .jsoniin
        """
        message = self.stringvar_to_string(message)

        self._messages[len(
            self._messages)] = f"{self.current_time_as_string()} {self._current_user}: {message}"
        save_to_file(self._messages)

        return 1


chat_services = ChatService()
