package com.example.nerdherd;

import android.content.Context;
import android.content.Intent;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Button;

public class ResetPasswordActivity extends AppCompatActivity {

    EditText newPassword;
    EditText confirmNewPassword;
    Button done_btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reset_password);

        newPassword = findViewById(R.id.new_password);
        confirmNewPassword = findViewById(R.id.confirm_new_password);
        done_btn = findViewById(R.id.done_btn);

        done_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = ResetPasswordActivity.this;
                String newPass = newPassword.getText().toString();
                String confNewPass = confirmNewPassword.getText().toString();

                if(newPass.equals(confNewPass)){
                    //TODO send new password to DB
                    Class mainActivity = MainActivity.class;
                    Intent intent = new Intent(context, mainActivity);
                    startActivity(intent);
                } else {
                    AlertDialog.Builder mismatchPasswords = new AlertDialog.Builder(context);
                    mismatchPasswords.setMessage("Passwords do not match");
                    mismatchPasswords.setCancelable(true);
                    mismatchPasswords.setPositiveButton("OK", null);
                    mismatchPasswords.create().show();
                }
            }
        });
    }

}
