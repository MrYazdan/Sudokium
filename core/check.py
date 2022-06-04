def run():
    """
        dependency checker!
    """
    try:
        import z3
        import webdriver_manager
        import selenium
    except:
        print('Dependency error! - please install requirements\n\t > pip install -r requirements')
