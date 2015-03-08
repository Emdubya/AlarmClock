<?php
ini_set('display_errors', 1);
error_reporting(E_ALL ^ E_NOTICE);

include('header.php');
?>
<div class="wrapper">
<div class="logowrapper">
<div class="logoleft"></div>
<div class="logoright"></div>
</div>
<?php
$alarm = shell_exec('sudo crontab -l -u pi | grep "subprocess20.py"');
$alarm = str_replace("sudo", "", $alarm);
$alarm = str_replace("python", "", $alarm);
$alarm = str_replace("/home/pi/subprocess20.py", "", $alarm);
$alarm = str_replace("> /dev/null 2>&1", "", $alarm);
echo "<center><h1>Currently configured alarm time - ". $alarm. "</h1></center>";
?>
<div class="center300">
<table>
<tr><td colspan="2"><h1>Set New Alarm</h1></td></tr>
<form method="post" action="index.php" name="alarm">
<tr><td><label for="minutes"><b>Minutes:</b> </label></td>
 <td> <input id="minutes" type="number" name="minutes" autocomplete="off" required></td></tr>
<tr><td><label for="hours"><b>Hours:</b> </label></td>
 <td> <input id="hours" type="number" name="hours" autocomplete="off" required></td></tr>
<tr><td><label for="day"><b>Day:</b> </label></td><td>
  <input id="day" type="text" name="day" autocomplete="off" required></td></tr>
<tr><td><label for="month"><b>Month:</b> </label></td><td>
  <input id="month" type="text" name="month" autocomplete="off" required></td></tr>
<tr><td><label for="weekday"><b>Weekday:</b> </label></td><td>
  <input id="weekday" type="text" name="weekday" autocomplete="off" required></td></tr>
</table>
<br /><br />
<input type="submit" id="submit" name="submit" /><br /><br />
</form>
</div>
<!--<div class="center300">
<h1> Light Control </h1>
<h2>All On</h2>
<form name="commandform">
        <input name="commandurl" type="hidden" value="http://192.168.1.120/api/newdeveloper/groups/0/action">
        <input name="messagebody" type="hidden" value="{'on':True}">
<button type="button" onclick="getHTML('PUT')">PUT</button>
</form>
<h2>All Off</h2>
<h2>Scene selection</h2>
</div> -->

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $SHELL = "SHELL=/bin/sh";
        $PATH = "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/etc:";
        $job = " ";
        $job .= $_POST['minutes'];
        $job .= " ";
        $job .= $_POST['hours'];
        $job .= " ";
        $job .= $_POST['day'];
        $job .= " ";
        $job .= $_POST['month'];
        $job .= " ";
        $job .= $_POST['weekday'];
        $job .= " ";
        $job .= "sudo python /home/pi/subprocess20.py > /dev/null 2>&1 ";
        file_put_contents('/tmp/crontab.txt', $SHELL .PHP_EOL);
        file_put_contents('/tmp/crontab.txt', $PATH, FILE_APPEND);
        file_put_contents('/tmp/crontab.txt', PHP_EOL . $job, FILE_APPEND);
        file_put_contents('/tmp/crontab.txt', PHP_EOL, FILE_APPEND);
        shell_exec('sudo crontab -u pi /tmp/crontab.txt');
        header( 'Location: index.php' ) ;
}
?>
</div>
<?php
include('footer.php');

?>
