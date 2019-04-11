package com.example.nerdherd;

import android.content.Context;
import android.content.Intent;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Button;

public class SendVerificationCodeActivity extends AppCompatActivity {

    EditText email;
    EditText confirm_email;
    Button verification_btn;
    Button login_btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_send_verification_code);

        email = findViewById(R.id.verification_email);
        confirm_email = findViewById(R.id.confirm_verification_email);
        verification_btn = findViewById(R.id.verification_btn);
        login_btn = findViewById(R.id.login_btn);

        verification_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = SendVerificationCodeActivity.this;
                String email_text = email.getText().toString().toLowerCase();
                String confirm_email_text = confirm_email.getText().toString().toLowerCase();
                if(email_text.equals(confirm_email_text)){
                    if(validEmail()){
                        //TODO send email
                        Class enterCodeActivity = EnterCodeActivity.class;
                        Intent intent = new Intent(context, enterCodeActivity);
                        startActivity(intent);
                    } else {
                        AlertDialog.Builder mismatchEmailAlert = new AlertDialog.Builder(context);
                        mismatchEmailAlert.setMessage("Email Address does not match one on record");
                        mismatchEmailAlert.setPositiveButton("OK", null);
                        mismatchEmailAlert.setCancelable(true);
                        mismatchEmailAlert.create().show();
                    }
                } else {
                    AlertDialog.Builder mismatchEmailAlert = new AlertDialog.Builder(context);
                    mismatchEmailAlert.setMessage("Emails do not match");
                    mismatchEmailAlert.setPositiveButton("OK", null);
                    mismatchEmailAlert.setCancelable(true);
                    mismatchEmailAlert.create().show();
                }
            }
        });

        login_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = SendVerificationCodeActivity.this;
                Class loginActivity = LoginActivity.class;
                Intent intent = new Intent(context, loginActivity);
                startActivity(intent);
            }
        });
    }


    public boolean validEmail(){
        return true;
    }
}
