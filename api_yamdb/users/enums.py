from enum import Enum


class UserRoles(Enum):
    """Класс-перечисления для выбора роли пользователя."""

    user = 'user'
    admin = 'admin'
    moderator = 'moderator'

    @classmethod
    def choices(cls):
        """Формируется соотвествие констант и значений."""
        return tuple((attribute.name, attribute.value) for attribute in cls)