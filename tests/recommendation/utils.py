import pendulum

from digipod import concepts as digipod_concepts
from digipod.concepts import OMOP_GENDER_FEMALE, OMOP_SURGICAL_PROCEDURE
from digipod.terminology import vocabulary as digipod_vocab
from digipod.tests.functions import (
    create_measurement,
    create_person,
    create_procedure,
    create_visit,
)


class Patient:

    _person = None
    _visits = []
    _measurements = []
    _procedures = []

    def __init__(self, gender_concept_id: int, birth_date: str):
        self._person = create_person(
            gender_concept_id=gender_concept_id,
            birth_date=pendulum.parse(birth_date).date(),
        )
        self._person.person_id = -1

    @property
    def person(self):
        return self._person

    def yield_objects(self) -> iter:
        for visit in self._visits:
            yield visit
        for measurement in self._measurements:
            yield measurement
        for procedure in self._procedures:
            yield procedure

    def add_intensive_care_visit(self, start: str, end: str) -> None:
        """
        Add an intensive care visit to the patient's record
        """
        self._visits.append(
            create_visit(
                person_id=self._person.person_id,
                visit_start_datetime=pendulum.parse(start),
                visit_end_datetime=pendulum.parse(end),
                visit_concept_id=digipod_concepts.OMOP_INTENSIVE_CARE,
            )
        )

    def add_inpatient_visit(self, start: str, end: str) -> None:
        """
        Add an inpatient visit to the patient's record
        """
        self._visits.append(
            create_visit(
                person_id=self._person.person_id,
                visit_start_datetime=pendulum.parse(start),
                visit_end_datetime=pendulum.parse(end),
                visit_concept_id=digipod_concepts.OMOP_INPATIENT_VISIT,
            )
        )

    def add_outpatient_visit(self, start: str, end: str) -> None:
        """
        Add an outpatient visit to the patient's record
        """
        self._visits.append(
            create_visit(
                person_id=self._person.person_id,
                visit_start_datetime=pendulum.parse(start),
                visit_end_datetime=pendulum.parse(end),
                visit_concept_id=digipod_concepts.OMOP_OUTPATIENT_VISIT,
            )
        )

    def add_surgery(self, start: str, end: str) -> None:
        """
        Add a surgical procedure to the patient's record
        """
        self._procedures.append(
            create_procedure(
                person_id=self._person.person_id,
                start_datetime=pendulum.parse(start),
                end_datetime=pendulum.parse(end),
                procedure_concept_id=OMOP_SURGICAL_PROCEDURE,
            )
        )

    def add_measurement(
        self,
        concept_id: int,
        datetime: str,
        value: float,
        unit_concept_id: int | None = None,
    ) -> None:
        """
        Add a measurement to the patient's record
        """
        self._measurements.append(
            create_measurement(
                person_id=self._person.person_id,
                measurement_concept_id=concept_id,
                measurement_datetime=pendulum.parse(datetime),
                value_as_number=value,
                unit_concept_id=unit_concept_id,
            )
        )

    def add_MMSE(self, datetime: str, score: int) -> None:
        """
        Add a Mini-Mental State Examination (MMSE) measurement to the patient's record
        """
        self.add_measurement(digipod_concepts.OMOP_MMSE, datetime, score)

    def add_nudesc(self, datetime: str, score: int) -> None:
        """
        Add a Nursing Delirium Screening Scale (NuDESC) measurement to the patient's record
        """
        self.add_measurement(digipod_vocab.NuDESC.concept_id, datetime, score)

    def add_at4(self, datetime: str, score: int) -> None:
        """
        Add a (4 A's Test) 4AT measurement to the patient's record
        """
        self.add_measurement(digipod_vocab.FourAT.concept_id, datetime, score)

    def add_cam(self, datetime: str, score: int) -> None:
        """
        Add a Confusion Assessment Method (CAM) measurement to the patient's record
        """
        self.add_measurement(digipod_vocab.CAM.concept_id, datetime, score)

    def add_drs(self, datetime: str, score: int) -> None:
        """
        Add a Delirium Rating Scale (DRS) measurement to the patient's record
        """
        self.add_measurement(digipod_vocab.DRS.concept_id, datetime, score)

    def add_dos(self, datetime: str, score: int) -> None:
        """
        Add a Delirium Observation Scale (DOS) measurement to the patient's record
        """
        self.add_measurement(digipod_vocab.DOS.concept_id, datetime, score)

    def add_camicu(self, datetime: str, score: int) -> None:
        """
        Add a Confusion Assessment Method for the Intensive Care Unit (CAM-ICU) measurement to the patient's record
        """
        self.add_measurement(digipod_vocab.CAM_ICU.concept_id, datetime, score)

    def add_dds(self, datetime: str, score: int) -> None:
        """
        Add a Delirium Detection Scale (DDS) measurement to the patient's record
        """
        self.add_measurement(digipod_vocab.DDS.concept_id, datetime, score)

    def add_icdsc(self, datetime: str, score: int) -> None:
        """
        Add an Intensive Care Delirium Screening Checklist (ICDSC) measurement to the patient's record
        """
        self.add_measurement(digipod_vocab.ICDSC.concept_id, datetime, score)

    def add_3dcam(self, datetime: str, score: int) -> None:
        """
        Add a 3-minute Diagnostic Interview for CAM-defined Delirium (3D-CAM) measurement to the patient's record
        """
        self.add_measurement(digipod_vocab.ThreeDCAM.concept_id, datetime, score)

    def add_ASA(self, datetime: str, score: int) -> None:
        """
        Add an American Society of Anesthesiologists (ASA) score measurement to the patient's record
        """
        self.add_measurement(digipod_concepts.OMOP_ASA, datetime, score)

    def add_CCI(self, datetime: str, score: int) -> None:
        """
        Add a Charlson Comorbidity Index (CCI) measurement to the patient's record
        """
        self.add_measurement(
            digipod_vocab.CHARLSON_COMORBIDITY_INDEX.concept_id, datetime, score
        )

    def add_MiniCOG(self, datetime: str, score: int) -> None:
        """
        Add a Mini-Cognitive Assessment Instrument (Mini-COG) measurement to the patient's record
        """
        self.add_measurement(digipod_concepts.OMOP_MINICOG.concept_id, datetime, score)

    def add_MoCA(self, datetime: str, score: int) -> None:
        """
        Add a Montreal Cognitive Assessment (MoCA) measurement to the patient's record
        """
        self.add_measurement(digipod_concepts.OMOP_MOCA.concept_id, datetime, score)

    def add_ACER(self, datetime: str, score: int) -> None:
        """
        Add an Addenbrooke's Cognitive Examination - Revised (ACER) measurement to the patient's record
        """
        self.add_measurement(
            digipod_vocab.ADDENBROOKE_COGNITIVE_EXAMINATION.concept_id, datetime, score
        )


class AdultPatient(Patient):
    def __init__(self):
        super().__init__(gender_concept_id=OMOP_GENDER_FEMALE, birth_date="1990-05-12")
