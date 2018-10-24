class file_meta_data:
    """ This initializes a model's fundamental characteristics """
    def __init__(self, model, year_released, catalog_type, financial_perspective):
        self.model=model
        self.year_released=year_released
        self.catalog_type=catalog_type
        self.financial_perspective=financial_perspective


    def __repr__(self):
        return "Model {}, Year {}, Catalog Type {}, Financial Perspective {}".format(self.model, self.year_released, self.catalog_type, self.financial_perspective)

class ilf(file_meta_data):
    """ *.l__ file (ILF) """

    def __repr__(self):
        return "*.l__ file for " + super().__repr__()

class inf(file_meta_data):
    """ *.i__ file (INF) """

    def __repr__(self):
        return "*.l__ file for " + super().__repr__()

class inx(file_meta_data):
    """ *x.__ file (INX) """
    def __init__(self, model, year_released, catalog_type, financial_perspective, file_shape):
        super().__init__(model, year_released, catalog_type, financial_perspective)
        self.file_shape=file_shape

    def __repr__(self):
        return "*.l__ file for " + super().__repr__() + ", and File Shape {}".format(self.file_shape)

class model13():
    """ This class is composed of file classes in the above section """
    def __init__(self, year_released):
        # 10K-PP
        self._ilf_10k_pp = ilf(13, year_released, 'stc', 'hybrid')
        self._inf_10k_pp = inf(13, year_released, 'stc', 'hybrid')
        self._inx_10k_pp = inx(13, year_released, 'stc', 'hybrid', 'rect')
        # 10K-FC
        self._ilf_10K_fc = ilf(13, year_released, 'stc', 'fatalities')
        self._inf_10K_fc = inf(13, year_released, 'stc', 'fatalities')
        self._inx_10K_fc = inx(13, year_released, 'stc', 'fatalities', 'rect')
        # Hist
        self._ilf_hist = ilf(13, year_released, 'hist', 'hybrid')
        self._inf_hist = inf(13, year_released, 'hist', 'hybrid')
        self._inx_hist = inx(13, year_released, 'hist', 'hybrid', 'rect')
        # World Scenarios
        self._ilf_ws = ilf(13, year_released, 'ws', 'hybrid')
        self._inf_ws = inf(13, year_released, 'ws', 'hybrid')
        self._inx_ws = inx(13, year_released, 'ws', 'hybrid', 'rect')
