from task_Barvynska import Driver

DRIVER_SVF = Driver("SVF", "Sebastian Vettel", "FERRARI", "12:02:58.917", "12:04:03.332", "1:04.415")
DRIVER_DRR = Driver("DRR", "Daniel Ricciardo", "RED BULL RACING TAG HEUER", "12:14:12.054", "12:11:24.067", "57:12.013")
LIST_DRIVERS_SORTED = [
    Driver("SVF", "Sebastian Vettel", "FERRARI", "12:02:58.917", "12:04:03.332", "1:04.415"),
    Driver("DRR", "Daniel Ricciardo", "RED BULL RACING TAG HEUER", "12:14:12.054", "12:11:24.067", "57:12.013")]
LIST_DRIVERS = [
    Driver("DRR", "Daniel Ricciardo", "RED BULL RACING TAG HEUER", "12:14:12.054", "12:11:24.067", "57:12.013"),
    Driver("SVF", "Sebastian Vettel", "FERRARI", "12:02:58.917", "12:04:03.332", "1:04.415")]

DICT_ABB = {
    "DRR": {"driver": "Daniel Ricciardo", "car": "RED BULL RACING TAG HEUER"},
    "SVF": {"driver": "Sebastian Vettel", "car": "FERRARI"},
}
DICT_TIME = {"SVF": "12:02:58.917", "DRR": "12:14:12.054"}

lIST_ALL_DRIVERS_DESC = [
    Driver('SVF', 'Sebastian Vettel', 'FERRARI', '12:02:58.917', '12:04:03.332', '1:04.415'),
    Driver('VBM', 'Valtteri Bottas', 'MERCEDES', '12:00:00.000', '12:01:12.434', '1:12.434'),
    Driver('SVM', 'Stoffel Vandoorne', 'MCLAREN RENAULT', '12:18:37.735', '12:19:50.198', '1:12.463'),
    Driver('KRF', 'Kimi RГ¤ikkГ¶nen', 'FERRARI', '12:03:01.250', '12:04:13.889', '1:12.639'),
    Driver('FAM', 'Fernando Alonso', 'MCLAREN RENAULT', '12:13:04.512', '12:14:17.169', '1:12.657'),
    Driver('CLS', 'Charles Leclerc', 'SAUBER FERRARI', '12:09:41.921', '12:10:54.750', '1:12.829'),
    Driver('SPF', 'Sergio Perez', 'FORCE INDIA MERCEDES', '12:12:01.035', '12:13:13.883', '1:12.848'),
    Driver('RGH', 'Romain Grosjean', 'HAAS FERRARI', '12:05:14.511', '12:06:27.441', '1:12.930'),
    Driver('PGS', 'Pierre Gasly', 'SCUDERIA TORO ROSSO HONDA', '12:07:23.645', '12:08:36.586', '1:12.941'),
    Driver('CSR', 'Carlos Sainz', 'RENAULT', '12:03:15.145', '12:04:28.095', '1:12.950'),
    Driver('NHR', 'Nico Hulkenberg', 'RENAULT', '12:02:49.914', '12:04:02.979', '1:13.065'),
    Driver('BHS', 'Brendon Hartley', 'SCUDERIA TORO ROSSO HONDA', '12:14:51.985', '12:16:05.164', '1:13.179'),
    Driver('MES', 'Marcus Ericsson', 'SAUBER FERRARI', '12:04:45.513', '12:05:58.778', '1:13.265'),
    Driver('LSW', 'Lance Stroll', 'WILLIAMS MERCEDES', '12:06:13.511', '12:07:26.834', '1:13.323'),
    Driver('KMH', 'Kevin Magnussen', 'HAAS FERRARI', '12:02:51.003', '12:04:04.396', '1:13.393'),
    Driver('LHM', 'Lewis Hamilton', 'MERCEDES', '12:18:20.125', '12:11:32.585', '53:12.460'),
    Driver('EOF', 'Esteban Ocon', 'FORCE INDIA MERCEDES', '12:17:58.810', '12:12:11.838', '54:13.028'),
    Driver('SSW', 'Sergey Sirotkin', 'WILLIAMS MERCEDES', '12:16:11.648', '12:11:24.354', '55:12.706'),
    Driver('DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '12:14:12.054', '12:11:24.067', '57:12.013')
                 ]
lIST_ALL_DRIVERS_ASC = [
        Driver('DRR', 'Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '12:14:12.054', '12:11:24.067', '57:12.013'),
        Driver('SSW', 'Sergey Sirotkin', 'WILLIAMS MERCEDES', '12:16:11.648', '12:11:24.354', '55:12.706'),
        Driver('EOF', 'Esteban Ocon', 'FORCE INDIA MERCEDES', '12:17:58.810', '12:12:11.838', '54:13.028'),
        Driver('LHM', 'Lewis Hamilton', 'MERCEDES', '12:18:20.125', '12:11:32.585', '53:12.460'),
        Driver('KMH', 'Kevin Magnussen', 'HAAS FERRARI', '12:02:51.003', '12:04:04.396', '1:13.393'),
        Driver('LSW', 'Lance Stroll', 'WILLIAMS MERCEDES', '12:06:13.511', '12:07:26.834', '1:13.323'),
        Driver('MES', 'Marcus Ericsson', 'SAUBER FERRARI', '12:04:45.513', '12:05:58.778', '1:13.265'),
        Driver('BHS', 'Brendon Hartley', 'SCUDERIA TORO ROSSO HONDA', '12:14:51.985', '12:16:05.164', '1:13.179'),
        Driver('NHR', 'Nico Hulkenberg', 'RENAULT', '12:02:49.914', '12:04:02.979', '1:13.065'),
        Driver('CSR', 'Carlos Sainz', 'RENAULT', '12:03:15.145', '12:04:28.095', '1:12.950'),
        Driver('PGS', 'Pierre Gasly', 'SCUDERIA TORO ROSSO HONDA', '12:07:23.645', '12:08:36.586', '1:12.941'),
        Driver('RGH', 'Romain Grosjean', 'HAAS FERRARI', '12:05:14.511', '12:06:27.441', '1:12.930'),
        Driver('SPF', 'Sergio Perez', 'FORCE INDIA MERCEDES', '12:12:01.035', '12:13:13.883', '1:12.848'),
        Driver('CLS', 'Charles Leclerc', 'SAUBER FERRARI', '12:09:41.921', '12:10:54.750', '1:12.829'),
        Driver('FAM', 'Fernando Alonso', 'MCLAREN RENAULT', '12:13:04.512', '12:14:17.169', '1:12.657'),
        Driver('KRF', 'Kimi RГ¤ikkГ¶nen', 'FERRARI', '12:03:01.250', '12:04:13.889', '1:12.639'),
        Driver('SVM', 'Stoffel Vandoorne', 'MCLAREN RENAULT', '12:18:37.735', '12:19:50.198', '1:12.463'),
        Driver('VBM', 'Valtteri Bottas', 'MERCEDES', '12:00:00.000', '12:01:12.434', '1:12.434'),
        Driver('SVF', 'Sebastian Vettel', 'FERRARI', '12:02:58.917', '12:04:03.332', '1:04.415')
                 ]

ASC_SVF = '<td style="background-color:rgb(127, 248, 127);">1</td>\n        '
'<td style="background-color:rgb(127, 248, 127);">SVF</td>\n'
DESC_SVF = '<td style="background-color:rgb(244, 122, 122);">19</td>\n        '
'<td style="background-color:rgb(244, 122, 122);">SVF</td>\n        '
'<td style="background-color:rgb(244, 122, 122);">Sebastian Vettel</td>\n'
DRR = '<tr>\n        <td>Daniel Ricciardo</td>\n        '
'<td><a href="/report/drivers/DRR" > DRR </a></td>\n    </tr>\n\n    <tr>\n'
