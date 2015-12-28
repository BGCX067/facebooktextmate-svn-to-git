<?php

//
//  ${TM_NEW_FILE_BASENAME}
//
//  Created by ${TM_USERNAME} on ${TM_DATE}.
//  Copyright (c) ${TM_YEAR} ${TM_ORGANIZATION_NAME}. All rights reserved.
//

include_once '../client/facebook.php';

$api_key = "${TM_FB_API}";
$secret = "${TM_FB_SECRET}";
$fb = new Facebook($api_key, $secret);

$fb->require_frame();
$user = $fb->require_login();

?>

