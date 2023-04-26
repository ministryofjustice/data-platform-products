from application.transform import generate_report
from unittest.mock import patch
import pandas as pd


class TestTransform(object):

    data = {"Date": ["Q3", "Q3", "Q3", "Q3"],
            "Outcomes": ["Dismissed", "Dismissed", "Dismissed", "Dismissed"],
            "Predominant function of establishment": ["Category A (High Security)", "Category B", "Category C",
                                                      "Local"],
            "Establishment": ["Belmarsh", "Belmarsh", "Frankland", "Frankland"],
            "Adjudicator": ["Governor", "Governor", "Governor", "Governor"],
            "Sex": ["M", "M", "M", "M"],
            "Age group": ["25 - 29", "30 - 39", "21 - 24", "30 - 39"],
            "Ethnicity": ["b Black/ African/ Caribbean/ Black British", "e White",
                          "c Mixed/ Multiple ethnic groups", "d Other ethnic group"],
            "Religion": ["b Muslim", "a Christian", "i No religion", "b Muslim"],
            "Offence": ["Disobedience/disrespect", "Disobedience/disrespect", "Unauthorised transactions",
                        "Unauthorised transactions"],
            "Detailed offence": ["Disobeys any lawful order", "Disobeys any lawful order", "Drug related offence",
                                 "Drug related offence"],
            "Count": [1, 1, 1, 1]
            }

    @patch('application.transform.get_data', return_value=pd.DataFrame.from_dict(data))
    def test_generate_report(self, mocked_table):
        expected_data = {"Establishment": ["Belmarsh", "Belmarsh", "Frankland", "Frankland"],
                         "Religion": ["a Christian", "b Muslim", "b Muslim", "i No religion"],
                         "Offence": ["Disobedience/disrespect", "Disobedience/disrespect", "Unauthorised transactions",
                                     "Unauthorised transactions"],
                         "Count": [1, 1, 1, 1]
                         }
        expected = pd.DataFrame.from_dict(expected_data)
        pd.testing.assert_frame_equal(generate_report(
            'fake_bucket', 'fake_key'), expected)
