from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class BuildDto:
    api = Namespace('build', description='building docker images')

    git_context = api.model('git_build_context', {
        'dir_name': fields.String(required=True, description='name of dir, where build context content will be saved, '
                                                             'relative to Dockerfile'),

        'url': fields.String(required=True, description='Git url'),
        'username': fields.String(required=False, description='username for git'),
        'password': fields.String(required=False, description='password for git')
    })

    build_params = api.model('build_params', {
        'source_type': fields.String(required=True, description='"Dockerfile" or "tar"'),
        'source_url': fields.Url(required=True, description='url of Dockerfile or tar'),
        'source_username': fields.Url(required=False, description='username for Dockerfile or tar'),
        'source_password': fields.Url(required=False, description='password for Dockerfile or tar'),
        'build_context': fields.List(required=False, description='Build context, if building from Dockerfile',
                                     cls_or_instance=fields.Nested(git_context)),
        'target_image_name': fields.String(required=True, description='desired docker image name'),
        'target_image_tag': fields.String(required=False, default='latest', description='desired docker image tag')
    })


class InfoDto:
    api = Namespace('info', description='Info about jobs')
    check_info = api.model('info_details', {
        'session_token': fields.String(required=True, description='Session token of image-building job')
    })


authorizations = {
    'Bearer token': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}
