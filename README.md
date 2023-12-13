# yandex_case_backend_2.0
API for utmn yandex case competition.
# Team 

███╗░░░███╗██╗░░░██╗███╗░░██╗██████╗░███████╗██╗░░██╗
████╗░████║██║░░░██║████╗░██║██╔══██╗██╔════╝╚██╗██╔╝
██╔████╔██║██║░░░██║██╔██╗██║██║░░██║█████╗░░░╚███╔╝░
██║╚██╔╝██║██║░░░██║██║╚████║██║░░██║██╔══╝░░░██╔██╗░
██║░╚═╝░██║╚██████╔╝██║░╚███║██████╔╝███████╗██╔╝╚██╗
╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝

# Used technologies:
    Frameworks:
      Django
      Django Rest Framework (DRF)
      Celery
    Databases:
      Postgresql (major db)
      Redis (celery broker)
    Other instruments:
      Git
      Docker + compose
      smtp.mail.ru (SMPT)

# API endpoints:
admin:

    admin/ 

auth:

    auth/users/
    auth/users/me/
    auth/token/login/
    auth/token/logout/

API:

    // events CRUD
    api/v1/events/
    api/v1/events/event_id/

    // list and retrieve users
    api/v1/users/
    api/v1/users/user_id/

    // relation CRUD
    api/v1/user-event-rel/
    api/v1/user-event-rel/rel_id/

    // category CRUD
    api/v1/categories/
    api/v1/categories/category_id/

# Mailing
This API uses smtp.mail.ru SMTP server.

1) Every time new relation between user and event is created it sends notification to user's email.

...more functionality in the future...