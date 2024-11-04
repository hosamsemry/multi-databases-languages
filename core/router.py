class LanguageDatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'core':
            return 'default'
        elif model._meta.app_label == 'news_ar':
            return 'arabic_db'
        elif model._meta.app_label == 'news_en':
            return 'english_db'
        elif model._meta.app_label == 'news_fr':
            return 'french_db'
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'core':
            return db == 'default'
        elif app_label == 'news_ar':
            return db == 'arabic_db'
        elif app_label == 'news_en':
            return db == 'english_db'
        elif app_label == 'news_fr':
            return db == 'french_db'
        return None
