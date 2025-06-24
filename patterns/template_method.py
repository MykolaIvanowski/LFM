from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process(self):
        self.load_data()
        self.clean_data()
        self.analyze_data()
        self.report()

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def clean_data(self):
        pass

    @abstractmethod
    def analyze_data(self):
        pass

    def report(self):
        print("Reporting results...")  # Hook method with default behavior

class CSVDataProcessor(DataProcessor):
    def load_data(self):
        print("Loading data from CSV")

    def clean_data(self):
        print("Cleaning CSV data")

    def analyze_data(self):
        print("Analyzing CSV data")

processor = CSVDataProcessor()
processor.process()