from django.test import TestCase
import requests

class test_json_data_home(TestCase):
    def setUp(self):
        self.response = requests.get('https://cefis.com.br/api/v1/event')

    def test_code_status(self):
        self.assertEqual(200, self.response.status_code)

class test_json_data_course_detail(TestCase):
    def setUp(self):
        self.response = requests.get('https://cefis.com.br/api/v1/event/1086?include=classes')

    def test_code_status(self):
        self.assertEqual(200, self.response.status_code)

    def test_json_data(self):
        json = '{"data":{"id":1086,"title":"Capta\u00e7\u00e3o de Recursos","subtitle":"(BNDES e FCO)","data_gravacao":null,"duracao_estimada":"00:00","teachers_names":"ALEXANDRE DAMASO","resume":"Neste curso iremos aprender sobre a Capta\u00e7\u00e3o de Recursos segundo o Banco Nacional de Desenvolvimento Econ\u00f4mico e Social, e tamb\u00e9m do Fundo Constitucional de Financiamento do Centro Oeste (BNDES e FCO). Os projetos e as vantagens que abrangem aos investidores ao obterem um financiamento de longo prazo.","start":1535752800,"end":1535756400,"color":0,"category":"Contabil","hours":0,"type":"all","watchLaterEvent":false,"buyed":false,"demo_showed":false,"streaming_url":"","banner":"https:\/\/cefiscdn.s3-sa-east-1.amazonaws.com\/media\/5329ef3029397fd445fcd867399ac8621534873013.jpg","video_promocional":"https:\/\/player.vimeo.com\/external\/120535176.mobile.mp4?s=3c393d914f425a5859edb742d4fb651e","free":false,"discount":false,"original_price":0,"price":0,"data_realizacao":"2018-08-31","data_lancamento":null,"live_date":"AO VIVO 31\/08\/2018","live":false,"live_now":false,"is_today":false,"video_divulgacao":"https:\/\/www.youtube.com\/embed\/iwJoxqOoZfM?rel=0","video_divulgacao_sources":null,"categories":[2,4],"keywords":["economia","eco","bndes","projeto","financiamento"],"internal":false,"transmission":null,"comments":false,"questions":false,"not_answered_questions":false,"status_contract":"accept","publish":"approved","available":"1","notifications":null,"instrutor_edit":"0","highlighted_trailer":"0","status_production":"doing","status":true,"duration":"00:00:00","duration_classes":"00:00:00","rated":false,"rating":0,"total_ratings":0,"quality_ratings":5,"total_student_ratings":0,"progress":null,"percentProgress":0,"watched":"00:00:00","editing":true,"target_group":"","content":"","goal":"Esse curso tem como objectivo desenvolver as habilidades do profissional na Capta\u00e7\u00e3o de recursos, pois ao longo dos anos muitas empresas participam ativamente do desenvolvimento da economia em nosso pa\u00eds.","parcels":"4","recorded_url":null,"banner_base":"https:\/\/cefiscdn.s3-sa-east-1.amazonaws.com\/media\/5329ef3029397fd445fcd867399ac8621534873013.jpg","meta_participantes":50,"has_one_video":false,"last_watched_log":null,"slides":false,"classes":[]}}'
        self.assertJSONEqual(json, self.response.text)
