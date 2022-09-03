<?php

    chmod("get_feature.py", 0755);
    $output = exec("python get_feature.py");
    echo $output;
    echo system("sudo -u osspcoconut python get_feature.py");
    echo system("python get_feature.py");
    echo system("whoami");
    echo "제발 되라";

?>