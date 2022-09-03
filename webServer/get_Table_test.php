<?php

    $db_host = "localhost"; 
    $db_user = "osspcoconut"; 
    $db_passwd = "";
    $db_name = "osspcoconut";

    // MySQL - DB 접속.
    $conn = mysqli_connect($db_host,$db_user,$db_passwd,$db_name);
    if (mysqli_connect_errno()){
        echo "MySQL 연결 오류: " . mysqli_connect_error();
        exit;
    } else {
        echo "DB : \"$db_name\"에 접속 성공.<br/>";
    }

    // 문자셋 설정, utf8.
    mysqli_set_charset($conn,"utf8"); 

    // 테이블 쿼리 후 내용 출력.
    $sql = "SELECT * FROM test";
    if ($result = mysqli_query($conn,$sql)){
        while($row = mysqli_fetch_array($result)){
            echo $row['name'];
            echo $row['student_id'];
        }
        mysqli_close($conn);
    } else {
        echo "테이블 쿼리 오류: " . mysqli_error($conn);
        exit;
    }
?>