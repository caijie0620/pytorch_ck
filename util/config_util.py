import os
from os.path import expanduser


def get_home_dir():
    return expanduser('~')


def get_exp_db_dir():
    home = get_home_dir()
    exp_db_dir = os.path.join(home, 'exp_db')
    return exp_db_dir


def get_processed_db_dir():
    home = get_home_dir()
    exp_db_dir = os.path.join(home, 'processed_db')
    return exp_db_dir


def get_models_dir(experiment_file, set_name = ''):
    tokens = experiment_file.split("/")
    # take filename(no-ext), dbname , and project name
    exp_dir = '/'.join(tokens[-3:])[:-3]
    exp_dir = os.path.join(
        get_exp_db_dir(),
        exp_dir
    )
    models_dir = os.path.join(
        exp_dir,
        set_name,
        'models'
    )
    return models_dir


def get_results_dir(experiment_file,set_name = ''):
    tokens = experiment_file.split("/")
    # take filename(no-ext), dbname , and project name
    exp_dir = '/'.join(tokens[-3:])[:-3]
    exp_dir = os.path.join(
        get_exp_db_dir(),
        exp_dir
    )
    results_dir = os.path.join(
        exp_dir,
        set_name,
        'results'
    )
    return results_dir


def get_gen_dir(experiment_file,set_name = ''):
    tokens = experiment_file.split("/")
    # take filename(no-ext), dbname , and project name
    exp_dir = '/'.join(tokens[-3:])[:-3]
    exp_dir = os.path.join(
        get_exp_db_dir(),
        exp_dir
    )
    results_dir = os.path.join(
        exp_dir,
        set_name,
        'gen'
    )
    return results_dir


def get_log_dir(experiment_file, set_name = ''):
    tokens = experiment_file.split("/")
    # take filename(no-ext), dbname , and project name
    exp_dir = '/'.join(tokens[-3:])[:-3]
    exp_dir = os.path.join(
        get_exp_db_dir(),
        exp_dir
    )
    log_dir = os.path.join(
        exp_dir,
        set_name
    )
    return log_dir

if __name__ == '__main__':
    print(get_home_dir())

