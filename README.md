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
# API endpoints:
admin:

    admin/ 

auth:

    auth/users/
    auth/users/me/
    auth/token/login/
    auth/token/logout/

API:

    api/v1/events/
    api/v1/events/event_id/
