def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users_avatar/user_{0}/{1}'.format(instance.user.id, filename)
