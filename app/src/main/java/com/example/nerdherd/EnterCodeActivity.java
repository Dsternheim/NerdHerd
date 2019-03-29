package com.example.nerdherd;

import android.content.Context;
import android.content.Intent;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class EnterCodeActivity extends AppCompatActivity {

    Button enter_btn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_enter_code);

        enter_btn = findViewById(R.id.enter_btn);

        enter_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = EnterCodeActivity.this;
                if(checkCode()){
                    // Go to reset password page
                    Class resetPasswordActivity = ResetPasswordActivity.class;
                    Intent intent = new Intent(context, resetPasswordActivity);
                    startActivity(intent);
                } else {
                    AlertDialog.Builder codeErrorAlert = new AlertDialog.Builder(context);
                    codeErrorAlert.setMessage("Incorrect Code");
                    codeErrorAlert.setPositiveButton("OK", null);
                    codeErrorAlert.setCancelable(true);
                    codeErrorAlert.create().show();
                }
            }
        });
    }

    public boolean checkCode(){
        return true;
    }
}
