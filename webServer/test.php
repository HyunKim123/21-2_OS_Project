<?php

$db_host = "localhost"; 
$db_user = "osspcoconut"; 
$db_passwd = "coconut1!";
$db_name = "osspcoconut";

// table 만들기
if(isset($_POST)){
    $name = $_POST['name'];
    $id = $_POST['student_id'];
    $conn = mysqli_connect($db_host,$db_user,$db_passwd,$db_name);

    if (mysqli_connect_errno()){
    echo "MySQL 연결 오류: " . mysqli_connect_error();
    exit;
    } else {
    echo "DB : \"$db_name\"에 접속 성공.<br/>";
    }
    $query = "INSERT INTO test(name, student_id) VALUES ('$name','$id')";
    if (mysqli_query($conn,$query)){
        echo "성공적으로 테이블을 만들었습니다.<br/>";
    } else {
        echo "테이블 쿼리 오류: " . mysqli_error($conn);
        exit;
    }
}
?> 