<?php


//set ui language
if ($lang == 'ger') {
    $ui_addcomment = 'Kommentar hinzufügen';
    $ui_yourname = 'Dein Name';
    $ui_message = 'Nachricht';
    $ui_submit = 'Absenden';
    $ui_noname = 'Du hast keinen Namen angegeben';
    $ui_nomessage = 'Du hast keine Nachricht eingegeben';
    $ui_time = '\A\m j. F Y \u\m  G:i \h\a\t ';
    $ui_said = ' gesagt:';
    $ui_nocomments = 'Derzeit sind noch keine Kommentare vorhanden.';
    $ui_reply = 'Antworten';
} else {
    $ui_addcomment = 'Leave a comment';
    $ui_yourname = 'Your name';
    $ui_message = 'Message';
    $ui_submit = 'Submit';
    $ui_noname = 'Please enter a name';
    $ui_nomessage = 'You did not enter a message';
    $ui_time = '\O\n F j, Y \a\t  g:i A ';
    $ui_said = ' said:';
    $ui_nocomments = 'So far, no comments have been posted.';
    $ui_reply = 'Reply';
}


if (isset($_POST['submit'])) {

    $_POST = array_map('stripslashes', $_POST);
    extract($_POST);

    if ($creator == '') {
        $error[] = $ui_noname;
    }

    if ($message == '') {
        $error[] = $ui_nomessage;
    } 

    if (isset($error)) {

        echo '<div id="errordiv">';

        foreach ($error as $errorline) {
            echo '<p style="text-align: center" class="error">' . $errorline . '</p>';
        }

        echo '</div>';

    } else {
        try {
            $message = str_replace($banned_phrases, $replace_phrases, $message);
            $creator = str_replace($banned_phrases, $replace_phrases, $creator);
			$message = preg_replace('/&gt;(\d+)/', '<a href="#com${1}">&gt;${1}</a>', $message);
            $message = nl2br($message);
            $stmt = $db->prepare('INSERT INTO comments (message,approved,site,postDate,creator) VALUES (:message, :approved, :site, :postDate, :creator)');
            $stmt->execute(array(
                ':message' => $message,
                ':approved' => true,
                ':site' => $id,
                ':creator' => $creator,
                ':postDate' => date('Y-m-d H:i:s')
            ));

            header('Location: #comment_box');
            exit;
        } catch (PDOException $e) {
            echo $e->getMessage();
        }
    }
}
?>

<h2 class="accent1" style="text-align: center; margin-top: 10rem;"><?php echo $ui_addcomment; ?></h2>

<form id='comment_box' class='add_comment' action='' method='post'>
    <p><label><?php echo $ui_yourname; ?></label><br/>
        <input type='text' name='creator' value='<?php if (isset($error)) {
            echo $_POST['creator'];
        } ?>'></p>

    <p><label><?php echo $ui_message; ?></label><br/>
        <textarea id=comment_input name='message' cols='60' rows='10'><?php if (isset($error)) {
                echo $_POST['message'];
            } ?></textarea></p>

    <p><input type='submit' name='submit' value='Submit'></p>
</form>

<div id="wrapper">

    <?php

    $num = 0;
    $stmt = $db->prepare('SELECT commentID, message, creator, site, postDate FROM comments WHERE site = :site AND approved = true ORDER BY commentID ASC');
    $stmt->execute(array(':site' => $id));
    while ($row = $stmt->fetch()) {
        if ($user->is_logged_in()) {
            echo '<form action="" style="text-align:right;margin-bottom:-3em" method="post">';
            echo '<input type="hidden" name="commentID" value=' . $row['commentID'] . '>';
            echo '<input class="error nuke" type="submit" name="hide" value="Hide">';
            echo '</form>';
        }

        if (in_array($row['creator'], $mods)) {
            $row['creator'] = '<span class="accent1">' . $row['creator'] . '</span>';
        }

        echo('<div class="comment_div"><p style="font-weight:600">' . date($ui_time, strtotime($row['postDate'])) . ' '
            . $row['creator'] . $ui_said . '<a id="com' . $row['commentID'] . '" style="font-size:60%;margin-left:3em;color:grey">(ID: ' .
            $row['commentID'] . ')</a><span class="reply fakelink" onclick="replyToComment(' . $row['commentID'] . ')">' . $ui_reply .
            '</span></p><p class="comment">' . $row['message'] . '</p></div><br><br>');
        $num++;
    }

    if ($num == 0) {
        echo '<p>' . $ui_nocomments . '</p>';
    }
    ?>

</div>
